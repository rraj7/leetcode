var events = require('events');
var eventEmitter = new events.EventEmitter();

var listner1 = function listner1 (){
    console.log("Listner 1 is executed");
}

var listner2 = function listner2 (){
    console.log("Listner 2 is executed");
}

eventEmitter.addListener('connection',listner1);
eventEmitter.on('connection',listner2);

var eventListners = require('events').EventEmitter.listenerCount(eventEmitter,'connection');

console.log(eventListeners + " Listner(s) listening to connection event");
eventEmitter.emit('connection');

eventEmitter.removeListener('connection', listner1);
console.log("Listner1 will not listen now.");

// Fire the connection event 
eventEmitter.emit('connection');

eventListeners = require('events').EventEmitter.listenerCount(eventEmitter,'connection');
console.log(eventListeners + " Listner(s) listening to connection event");

console.log("Program Ended.");