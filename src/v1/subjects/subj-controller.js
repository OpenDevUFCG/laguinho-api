import express from 'express';
import { loadSubjects, loadSubjectsRelationships } from './subj-data';

const router = express.Router();

router.get('/', async (req, res) => {
    res.json(await loadSubjects());
});

router.get('/relationships', async (req, res) => {
    res.json(await loadSubjectsRelationships());
});

export default router;