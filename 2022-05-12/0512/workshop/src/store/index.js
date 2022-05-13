import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    todos: []
  },
  getters: {
    allTodosCount: function (state) {
      return state.todos.length
    },
    completedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === false
      }).length
    }
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      // console.log(state)
      // console.log(todoItem)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO: function(state, todoItem) {
      //3. 배열의 각 요소에 함수가 적용된 새로운 배열을 state의 todos 할당
      state.todos = state.todos.map(todo => {
        //1. 넘어온 todoItem과 현재 todos의 요소가 일치 하면
        if (todo === todoItem) {
          // 2. isCompleted 상태를 변경한 새로운 object를 return
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    }
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      // const commit = context.commit
      // const { commit } = context
      // commit('CREATE_TODO', todoItem)
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem){
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function ({ commit }, todoItem){
      commit('UPDATE_TODO', todoItem)
    }
  },
  modules: {
  }
})
