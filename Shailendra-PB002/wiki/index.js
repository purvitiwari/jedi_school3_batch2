var request = require('http');
request.get({
        host: 'https://www.wikidata.org',
        path: '/w/api.php?action=wbsearchentities&search=amitabh%20bachhan&language=en&limit=20&format=json'
    }, function(response) {
        // Continuously update stream with data
        var body = '';
        response.on('data', function(d) {
            body += d;
        });
        response.on('end', function() {

            // Data reception is done, do whatever with it!
            var parsed = JSON.parse(body);
            console.log(parsed);
        });
    });