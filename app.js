/* Shows version of OWL Framework 
(function () {
  console.log("hello owl", owl.__info__.version);
})();*/
const { Component, mount , Store } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState , useStore } = owl.hooks;
// -------------------------------------------------------------------------
// Store
// -------------------------------------------------------------------------
const actions = {
  addTask({ state }, title) {
    title = title.trim();
    if (title) {
      const task = {
        id: state.nextId++,
        title: title,
        isCompleted: false,
      };
      state.tasks.push(task);
    }
  },
  toggleTask({ state }, id) {
    const task = state.tasks.find((t) => t.id === id);
    task.isCompleted = !task.isCompleted;
  },
  deleteTask({ state }, id) {
    const index = state.tasks.findIndex((t) => t.id === id);
    state.tasks.splice(index, 1);
  },
};
const initialState = {
  nextId: 1,
  tasks: [],
};
// -------------------------------------------------------------------------
// Task Component
// -------------------------------------------------------------------------
const TASK_TEMPLATE = xml/* xml */ `
    <div class="task" t-att-class="props.task.isCompleted ? 'done' : ''">
        <input type="checkbox" t-att-checked="props.task.isCompleted"
                t-on-click="dispatch('toggleTask', props.task.id)"/>
        <span><t t-esc="props.task.title"/></span>
        <span class="delete" t-on-click="dispatch('deleteTask', props.task.id)">🗑</span>
    </div>`;

class Task extends Component {
  static template = TASK_TEMPLATE;
  static props = ["task"];
  dispatch = useDispatch();
}
// -------------------------------------------------------------------------
// App Component
// -------------------------------------------------------------------------
const APP_TEMPLATE = xml/* xml */ `
    <div class="todo-app">
        <input placeholder="Enter a new task" t-on-keyup="addTask" t-ref="add-input"/>
        <div class="task-list">
            <t t-foreach="tasks" t-as="task" t-key="task.id">
                <Task task="task"/>
            </t>
        </div>
    </div>`;

class App extends Component {
  static template = APP_TEMPLATE;
  static components = { Task };

  
  inputRef = useRef("add-input");
  tasks = useStore((state) => state.tasks);
  dispatch = useDispatch();

  mounted() {
    this.inputRef.el.focus();
  }

  addTask(ev) {
    // 13 is keycode for ENTER
    if (ev.keyCode === 13) {
      this.dispatch("addTask", ev.target.value);
      ev.target.value = "";
    }
  }
}
// Setup code
function setup() {
   owl.config.mode = "dev";
   const store = new Store({ actions, state: initialState });
  App.env.store = store;
   const mountapp = new App(); //object to use mount mtd
   mountapp.mount(document.body);
//   App.env.store = makeStore();
}

whenReady(setup);
