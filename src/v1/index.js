import express from 'express';
import repoRouter from './repositories/repo-controller';

const router = express.Router();

router.use('/repositories', repoRouter);

export default router;