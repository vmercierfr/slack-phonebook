function linkDownload(downloader, filename, content) {
    /**
     * Set download link settings
     * @param {String} downloader - Reference to HTML element
     * @param {String} filename - Filename of the file to download
     * @param {String} content - Content of the file
     */
    contentType =  'data:application/octet-stream,';
    uriContent = contentType + encodeURIComponent(content);
    downloader.setAttribute('href', uriContent);
    downloader.setAttribute('download', filename);
}

function download(filename, content) {
    /**
     * Force to download of the specified content
     * @param {String} filename - Filename of the file to download
     * @param {String} content - Content of the file
     */
    var downloader = document.createElement('a');
    linkDownload(downloader, filename, content);
    document.body.appendChild(downloader);
    downloader.click();
    document.body.removeChild(downloader);
}

function vcard(id, firstname, lastname, title, email, phone) {
    /**
     * Download vcard
     * @param {Number} firstname - User id
     * @param {String} lastname - Firstname
     * @param {String} title - Title
     * @param {String} email - Email
     * @param {String} phone - Phone
     */
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