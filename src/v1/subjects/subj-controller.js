import express from 'express';
import loadSubjects from './subj-data';

const router = express.Router();

router.get('/', async (req, res) => {
    res.json(await loadSubjects());
});

export default router;