import csvtojson from 'csvtojson';

export default async function loadSubjects() {
    const csvFilePath = './src/v1/subjects/subj-data.csv';
    return await csvtojson().fromFile(csvFilePath);
};