import express from 'express';
import cors from 'cors';
import 'dotenv/config';

import v1Router from './v1';

const port = process.env.LAGUINHO_PORT || 8080;
const app = express();

app.use(cors());

app.use('/v1', v1Router);

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
