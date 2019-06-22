import express from 'express';
import repositoriosRouter from './repositorios/repositorios-controller';
import disciplinasRouter from './disciplinas/disciplinas-controller'

const router = express.Router();

router.use('/repositorios', repositoriosRouter);
router.use('/disciplinas', disciplinasRouter)

export default router;