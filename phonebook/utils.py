# -*- coding: utf-8 -*-

import os
import phonenumbers
from slackclient import SlackClient

def get_users(app):
    USERS_BLACKLIST = os.getenv('USERS_BLACKLIST', '').split(',')

    SLACK_TOKEN = os.getenv('SLACK_TOKEN')
    if not SLACK_TOKEN:
        raise Exception('SLACK_TOKEN not defined!')
    sc = SlackClient(SLACK_TOKEN)

    try:
        users = sc.api_call("users.list")['members']
    except Exception:
        raise Exception('Can not get Slack user list!')

    # Get users and keep only active members
    active_users = []

    # Compute users list
    for user in users:
        # Exclude deleted users
        if user['deleted'] == True:
            app.logger.debug('Skip deleted user: %s', user['name'])
            continue
        # Exclude bot users
        if user['is_bot'] == True:
            app.logger.debug('Skip bot user: %s', user['name'])
            continue
        # Exclude users in blacklist
        if user['name'] in USERS_BLACKLIST:
            app.logger.debug('Skip blacklisted user: %s', user['name'])
            continue
        # Format phone number
        if 'phone' in user['profile'] and user['profile']['phone']:
            try:
                phone_number = phonenumbers.parse(user['profile']['phone'], "FR")
                user['profile']['phone'] = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
                user['profile']['phone_link'] = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
            except Exception:
                app.logger.warning('Invalid phone number "%s" for user "%s"!', user['profile']['phone'], user['name'])
        # According to Slack documentation (https://api.slack.com/methods/users.list),
        # Only the image_* fields are guaranteed to be included in user profile
        # So we need to check all user profile fields
        active_users.append({
            'id': user['id'],
            'team_id': user['team_id'],
            'name': user['name'],
            'deleted': user['deleted'],
            #'status': user['status'],
            'real_name': user['real_name'],
            'tz': user['tz'],
            'tz_label': user['tz_label'],
            'tz_offset': user['tz_offset'],
            'profile': {
                'first_name': user['profile'].get('first_name', ''),
                'last_name': user['profile'].get('last_name', ''),
                'avatar_hash': user['profile'].get('avatar_hash', ''),
                'title': user['profile'].get('title', ''),
                'phone': user['profile'].get('phone', ''),
                'phone_link': user['profile'].get('phone_link', ''),
                'skype': user['profile'].get('skype', ''),
                'image_24': user['profile'].get('image_24', ''),
                'image_32': user['profile'].get('image_32', ''),
                'image_48': user['profile'].get('image_48', ''),
                'image_72': user['profile'].get('image_72', ''),
                'image_192': user['profile'].get('image_192', ''),
                'image_512': user['profile'].get('image_512', ''),
                'image_1024': user['profile'].get('image_1024', ''),
                'image_original': user['profile'].get('image_original', ''),
                'real_name': user['profile'].get('real_name', ''),
                'real_name_normalized': user['profile'].get('real_name_normalized', ''),
                'email': user['profile'].get('email', ''),
            },
            'is_admin': user['is_admin'],
            'is_owner': user['is_owner'],
            #'is_primary_owner': user['is_primary_owner'],
            #'is_restricted': user['is_restricted'],
            #'is_ultra_restricted': user['is_ultra_restricted'],
            'is_bot': user['is_bot'],
            #'has_2fa': user['has_2fa'],
            #'two_factor_type': user['two_factor_type']
        })
    return active_users
