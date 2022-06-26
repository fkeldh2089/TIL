<template>
  <div id="app">
    <h1>TodoList</h1>
    <h2>All TODO: {{ allTodosCount }}</h2>
    <h2>Completed TODO : {{ completedTodosCount }} </h2>
    <h2>Uncompleted TODO : {{ uncompletedTodosCount }} </h2>
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
import { mapGetters } from 'vuex'


export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm
  },
  computed: {
    ...mapGetters(['completedTodosCount', 'uncompletedTodosCount', 'allTodosCount'])
    // completedTodosCount: function() {
    //   return this.$store.getters.completedTodosCount
    // }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
