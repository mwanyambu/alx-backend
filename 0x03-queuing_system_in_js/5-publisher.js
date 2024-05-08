#!/usr/bin/node
/**
 * connect to redis
 */
import { createClient } from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.PUBLISH('holberton school channel', message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
