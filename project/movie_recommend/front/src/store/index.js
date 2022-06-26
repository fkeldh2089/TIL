import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import movies from './modules/movies'
import main from './modules/main'

Vue.use(Vuex)

export default new Vuex.Store({

  modules: { accounts, movies, main }
})
