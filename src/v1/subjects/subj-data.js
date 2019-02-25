import csvtojson from 'csvtojson';
import axios from 'axios';

export default async function loadSubjects() {
    const csvFilePath = 'https://raw.githubusercontent.com/OpenDevUFCG/roadmap-cc/master/data/disciplinas-ppc-2017.csv';
    return await csvtojson().fromString((await axios.get(csvFilePath)).data)
}