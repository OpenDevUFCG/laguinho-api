import express from 'express';
import { getRepositories } from './github';
 
const router = express.Router();

router.get('/', async (req, res) => {
    const quantity = req.query.quantity;
    const after = req.query.after;
    const repos = await getRepositories(quantity, after)
    res.json(repos);
});

export default router;