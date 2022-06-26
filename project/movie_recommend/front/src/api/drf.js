const HOST = 'http://localhost:8000/'
const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'


export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    update: () => HOST + ACCOUNTS + 'update/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },

  movies: {
    movies: () => HOST + MOVIES,
    movieDetail: moviePk => HOST + MOVIES + `${moviePk}/`,
    movieReview: moviePk => HOST + MOVIES + `${moviePk}/` + 'moviereview/',


    finalMovie: () => HOST + MOVIES + 'finalmovie/',
    yearAgo: () => HOST + MOVIES + 'yearago/',
    firstSetting: () => HOST + MOVIES + 'firstsetting/',
    manyGenre: () => HOST + MOVIES + 'manygenre/',
    voteGenre: () => HOST + MOVIES + 'votegenre/',
    eastAsia: () => HOST + MOVIES + 'eastasia/',
    hardTravel: () => HOST + MOVIES + 'hardtravel/',
    asiaOceania: () => HOST + MOVIES + 'asiaoceania/',
  },
}
