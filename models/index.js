var	mongoose 	= require('mongoose'),
	dotenv		= require('dotenv');

dotenv.config();

mongoose.set('debug', true);
mongoose.connect(process.env.DATABASE);
console.log(process.env.DATABASE);
mongoose.promise = Promise;

module.exports.Settings = require('./settings');
module.exports.Stats 	= require('./statistics');
module.exports.Data     = require('./data');
