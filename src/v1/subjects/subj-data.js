import csvtojson from 'csvtojson';
import request from 'request';

export default async function loadSubjects() {
    const csvFilePath = 'https://raw.githubusercontent.com/OpenDevUFCG/roadmap-cc/master/data/disciplinas-ppc-2017.csv';
 
    return await csv().fromStream(request.get(csvFilePath))
}