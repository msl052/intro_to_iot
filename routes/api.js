var express         = require('express'),
    router          = express.Router(),
    db              = require('../models'),
    dataHelpers     = require('../helpers/data');
    //statHelpers     = require('../helpers/statisitics'),
    //settingsHelpers = require('../helpers/settings');

/******** sensor readings **********/

router.route('/data')
    .get(dataHelpers.getData)
    .post(dataHelpers.createData)
    .delete(dataHelpers.deleteData);
/*
router.route('/data/:id')
    .get(dataHelpers.getOneData)
    .put(dataHelpers.editData)
    .delete(dataHelpers.deleteOneData);

router.route('/statistics')
    .get(statHelpers.getStats)
    .put(statHelpers.editStats)
    .delete(statHelpers.resetStats);

router.route('/settings')
    .get(settingsHelpers.getData)
    .put(settingsHelpers.editData);
*/
module.exports = router;

