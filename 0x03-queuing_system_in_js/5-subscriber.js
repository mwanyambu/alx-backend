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

const listener = (message) => console.log(message);
client.SUBSCRIBE('holberton school channel');

client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      client.UNSUBSCRIBE();
      client.QUIT();
    }
    listener(message);
  }
});
