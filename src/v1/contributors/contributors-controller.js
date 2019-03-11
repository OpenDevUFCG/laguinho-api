import express from 'express';
import getContributors from './getContributors';

const router = express.Router();

router.get('/', async (req, res) => {
    const contributors = await getContributors();
    res.json(contributors);
});

export default router;
