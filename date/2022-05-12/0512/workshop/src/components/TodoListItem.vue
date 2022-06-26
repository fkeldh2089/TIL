<template>
  <div>
    <span 
      @click="updateTodo(todo)"
      :class="{'is-completed': todo.isCompleted}"
    >{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
  
</template>

<script>
import { mapActions } from 'vuex'


export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodo'])

    // deleteTodo: function () {
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodo: function () {
    //   this.$store.dispatch('updateTodo', this.todo)
    // }
  }

}
</script>

<style>
.is-completed {
  text-decoration: line-through;
}
</style>