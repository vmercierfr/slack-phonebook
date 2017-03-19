function linkDownload(a, filename, content) {
    contentType =  'data:application/octet-stream,';
    uriContent = contentType + encodeURIComponent(content);
    a.setAttribute('href', uriContent);
    a.setAttribute('download', filename);
}

function download(filename, content) {
    var a = document.createElement('a');
    linkDownload(a, filename, content);
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function vcard(id, firstname, lastname, title, email, phone) {
    var vcard = 'BEGIN:VCARD\n';
    vcard = vcard + 'VERSION:4.0\n';
    vcard = vcard + "N:" + lastname + ';' + firstname + ';;;\n';
    vcard = vcard + "FN:" + firstname + ' ' + lastname + '\n';
    vcard = vcard + 'TITLE:' + title + '\n';
    vcard = vcard + 'ORG:' + 'CALLR' + '\n';
    vcard = vcard + 'TEL;Work:' + phone + '\n';
    vcard = vcard + 'EMAIL;Work:' + email + '\n';
    vcard = vcard + 'REV:20090401T065518' + '\n';
    vcard = vcard + 'VERSION:2.1' + '\n';
    vcard = vcard + 'CATEGORIES:Work' + '\n';
    vcard = vcard + 'END:VCARD';
    download(id + '.vcard', vcard);
}