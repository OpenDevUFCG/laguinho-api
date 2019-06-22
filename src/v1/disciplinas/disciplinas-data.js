import csvtojson from 'csvtojson';
import axios from 'axios';

const basePath = 'https://raw.githubusercontent.com/OpenDevUFCG/roadmap-cc/development/data'

async function loadSubjects() {
    const csvFilePath = `${basePath}/disciplinas-ppc-2017.csv`;
    return await csvtojson().fromString((await axios.get(csvFilePath)).data)
}

async function loadSubjectsRelationships() {
    const csvFilePath = `${basePath}/relacionamentos-disciplinas-ppc2017.csv`;
    return await csvtojson().fromString((await axios.get(csvFilePath)).data)
}

export {
    loadSubjects,
    loadSubjectsRelationships
}