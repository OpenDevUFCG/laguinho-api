import express from 'express';
import repoRouter from './repositories/repo-controller';
import subjRouter from './subjects/subj-controller';
import contriRouter from './contributors/contributors-controller';

const router = express.Router();

router.use('/repositories', repoRouter);
router.use('/subjects', subjRouter);
router.use('/contributors', contriRouter);

export default router;
