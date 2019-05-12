import express from 'express';
import { getRepositories } from './github';
 
const router = express.Router();

router.get('/', async (req, res) => {
    const quantity = req.query.quantidade;
    const after = req.query.apos;
    const repos = await getRepositories(quantity, after)
    res.json(repos);
});

export default router;