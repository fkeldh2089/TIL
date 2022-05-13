<template>
  <div>
    <input
      type="text"
      v-model="todoTitle"
      >
      <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      // console.log('todo 생성')
      // this.$store.commit('CREATE_TODO', todoItem)
      if(todoItem.title){
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>