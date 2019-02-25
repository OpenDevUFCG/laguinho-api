import express from 'express';
import repoRouter from './repositories/repo-controller';
import subjRouter from './subjects/subj-controller'

const router = express.Router();

router.use('/repositories', repoRouter);
router.use('/subjects', subjRouter)

export default router;