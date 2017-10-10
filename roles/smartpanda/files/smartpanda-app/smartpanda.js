var http = require('http');
var config = require('./config.json');
var HttpDispatcher = require('httpdispatcher');
var dispatcher = new HttpDispatcher();
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://ori:daba@ds013405.mlab.com:13405/panda";

function getNumOfDocs (collectionName, callback) {
    MongoClient.connect(url, function (error, db){
        if(error) return callback(err);

        db.collection(collectionName).count({}, function(error, numOfDocs){
            if(error) return callback(err);

            db.close();
            callback(null, numOfDocs);
        });
    }); 
};

function handleRequest(request, response){
    try {
        console.log("Requested URL: " + request.url);
        dispatcher.dispatch(request, response);
    } catch(err) {
        console.log(err);
    }
};

dispatcher.onGet("/smart-panda", function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    getNumOfDocs("gets", function(err, count) {
    if (err) {
       return console.log(err.message);
    }
    res.end('Random gangsta panda pics served ' + count + ' times!\n');
    //console.log('number of documents', count);
    });
});

dispatcher.onError(function(req, res) {
        res.writeHead(404);
        res.end("404 - Page Does not exists");
});

http.createServer(handleRequest).listen(config.port, function(){
    console.log("Server listening on: http://localhost:%s", config.port);
});
