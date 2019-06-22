import express from 'express';
import { loadSubjects, loadSubjectsRelationships } from './disciplinas-data';

const router = express.Router();

router.get('/', async (req, res) => {
    res.json(await loadSubjects());
});

router.get('/relacionamentos', async (req, res) => {
    res.json(await loadSubjectsRelationships());
});

export default router;