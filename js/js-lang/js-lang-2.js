"use strict";

// functions

function subtract(x, y) {
    console.log(x, y);
    return x - y;
}

function add(x, y=0) {
    return x + y;
}

function getArg(a) {
    return a;
}

const subtractArrow = (x, y) => {
    return x - y;
};

const addArrow = (x, y) => x + y;


// objects

const melonCodes = {
    cren: 'Crenshaw',
    musk: 'Muskmelon'
};

const cat = {
    name: 'Marvin',
    age: 2,
    'favorite smell': 'cotton'
};


const capitals = { 'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    Arkansas: 'Little Rock',
    California: 'Sacramento',
    Colorado: 'Denver',
    Connecticut: 'Hartford',
    Delaware: 'Dover',
    Florida: 'Tallahassee',
    Georgia: 'Atlanta',
    Hawaii: 'Honolulu',
    Idaho: 'Boise',
    Illinois: 'Springfield',
    Indiana: 'Indianapolis',
    Iowa: 'Des Moines',
    Kansas: 'Topeka',
    Kentucky: 'Frankfort',
    Louisiana: 'Baton Rouge',
    Maine: 'Augusta',
    Maryland: 'Annapolis',
    Massachusetts: 'Boston',
    Michigan: 'Lansing',
    Minnesota: 'Saint Paul',
    Mississippi: 'Jackson',
    Missouri: 'Jefferson City',
    Montana: 'Helena',
    Nebraska: 'Lincoln',
    Nevada: 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
};

const melon = {
    commonName: 'watermelon',
    color: 'green',
    price: 2.0
};

const num1 = 24;
const num2 = 42;
const nums = {num1, num2};

// sets

const set2 = new Set();

const set3 = new Set(['a', 'b']);
