import { getAxiosInstance } from '../repositories/github';
import projects from '../repositories/repo-data';

/**
 * Recupera as contribuições em todos os repositórios
 * @returns {Array<Object>} Array de contribuidores
 */
const getContributors = async () => {
    const { repositories } = projects;
    const orgRepos = await getOrgRepos();
    const allRepositories = repositories.concat(orgRepos);
    const eachRepoContri = await Promise.all(allRepositories.map(repo => getRepoContributors(repo.name)));
    return mergeContributions(eachRepoContri);
};

/**
 * Recupera os nomes dos repositórios da OpenDev
 * 
 * @returns {Array<Object>} Array com nomes dos repositórios
 *                          para concatenar com os dos dados
 */
const getOrgRepos = async () => {
    let repos = await getAxiosInstance().get(`/orgs/${projects.org}/repos`);
    repos = repos.data.map(repo => ({ name: repo.full_name }));
    return repos;
};

/**
 * Recupera contribuidores do repositório
 * 
 * @param {String} nameWithOwner Nome do usuário e do
 *                 repositório: (username/repository)
 * @returns {Array<Object>} Contribuidores do repositório
 */
const getRepoContributors = async nameWithOwner => {
    let contributors = await getAxiosInstance().get(`/repos/${nameWithOwner}/contributors`);
    contributors = contributors.data;
    contributors = await Promise.all(contributors.map(contributor => transformContributor(contributor)));
    return contributors;
};

/**
 * Recupera o nome do usuário
 * 
 * @param {String} username do usuário cujo nome deve ser recuperado
 * @returns {String} nome do usuário
 */
const getUsersName = async username => {
    const user = await getAxiosInstance().get(`/users/${username}`);
    const { name } = user.data;
    return name;
};

/**
 * Mapeia o contribuidor retornado pelo GitHub para o objeto com os
 * atributos que desejamos.
 * 
 * @param {Object} contributor - Objeto de contribuidor retornado pelo github
 * @returns {Object} contribuidor com os atributos que precisamos
 */
const transformContributor = async contributor => ({
    username: contributor.login,
    name: await getUsersName(contributor.login),
    githubUrl: contributor.url,
    avatar: contributor.avatar_url,
    contributions: contributor.contributions
});

/**
 * Transforma a matriz de contribuidores num array de contribuidores,
 * somando suas contribuições
 * 
 * @param {Array<Array<Object>>} eachRepoContri Array com os arrays
 *                               de contribuidores de cada repositório
 * @returns {Array<Object>} Array de contribuidores
 */
const mergeContributions = eachRepoContri => {
    const allRepoContri = {};
    eachRepoContri.forEach(repoContri => {
        repoContri.forEach(contributor => {
            if (allRepoContri[contributor.username] !== undefined) {
                allRepoContri[contributor.username].contributions += contributor.contributions;
            } else {
                allRepoContri[contributor.username] = contributor;
            }
        });
    });
    return Object.keys(allRepoContri).map(key => allRepoContri[key]);
};

export default getContributors;
