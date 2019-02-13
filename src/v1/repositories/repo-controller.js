import express from 'express';

const router = express.Router();

router.get('/', (req, res) => {
    // TODO Fetch the repositories from OpenDevUFCG and the ones listed on ufcg-repo-data.js
    res.json({text: "Hello World"});
});

export default router;