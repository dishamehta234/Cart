const { Component, Store, mount } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useState, useDispatch, useStore } = owl.hooks;
const actions = {
		addTask({ state }, p_id) {
		        if (p_id && (!state.tasks.find(t => parseInt(t.p_id) == parseInt(p_id)))) {
		            const newTask = {
		                p_id: p_id,
		            };
		            state.tasks.push(newTask);
			   	}
		},

		deleteTask({ state }, p_id) {
		    const index = state.tasks.findIndex((t) => t.p_id == p_id);
		    state.tasks.splice(index, 1);
		}
};
	const initialState = {
	  tasks: [],
	};




const APP_TEMPLATE = xml /* xml */`
<div class="container">

			<div class="header" align="right">Shopping App
			  	<input id="searchdata" placeholder="Search product.." t-on-keyup="searchFunction"/>
			</div>

			<div id="alltask">
				<t t-foreach="products" t-as="product" t-key="product.id">	
					<div class="products" id="task">
						<span>
							<t t-esc="product.product_name"/>
						</span>
						<span class="priceprd">
							Rs.<t t-esc="product.product_price"/>
						</span>
						<div class="btn">
							<button class="btn" type="button" t-att-id="product.id" t-on-click="addTask">Add to cart</button>
						</div>
					</div> 
				</t>
			</div>
			<div class="cartitems">
					<h2>Total Cart Products</h2>
					<span>
						<t t-set="total" t-value="0"/>
					</span>
					<t t-foreach="tasks" t-as="task" t-key="task.id">
						<span>
							<t t-set="total" t-value="total + products[task.p_id-1].product_price"/>
						</span>
						<span>
							<t t-esc="products[task.p_id-1].product_name"/>
						</span>
						<span class="delete" t-att-id="task.p_id" t-on-click="deleteTask">🗑</span><br></br>
					</t>
					<div class="amttotal" align="right">
						<span><b>Total price : <t t-esc="total"/></b></span>
					</div>
			</div>
</div>`;
	// Owl Components
	class App extends Component {
	    static template = APP_TEMPLATE;

	tasks = useStore((state) => state.tasks);
    dispatch = useDispatch();


	    addTask(ev) {
	        if (ev.target.id) {
		        this.dispatch("addTask", ev.target.id)
		       	}
		}
	    deleteTask(ev) {
		    this.dispatch("deleteTask", ev.target.id)
		}

		searchFunction() {
            var input, filter, main, div, div2, i, inputValue;
            input = document.getElementById("searchdata").value;
            filter = input.toUpperCase();
            main = document.getElementById("alltask");
            div = main.getElementsByClassName("task");
            for (i = 0; i < div.length; i++) {
                div2 = div[i].getElementsByTagName("span")[0];
                if (div2) {
                    inputValue = div2.textContent || div2.innerText;
                    if (inputValue.toUpperCase().indexOf(filter) > -1) {
                        div[i].style.display = "";
                    } else {
                        div[i].style.display = "none";
                    }
                }
            }
        }


	  products = [
	    {
	      "id": 1,
	      "product_name": "Alover Jell",
	      "product_price": 100,
	    },
	    {
	      "id": 2,
	      "product_name": "Milk Protein Shampoo",
	      "product_price": 200,
	    },
	    {
	      "id": 3,
	      "product_name": "Natural Alover Shampoo",
	      "product_price": 500,
	    },
	    {
	      "id": 4,
	      "product_name": "Alover Body Lotion",
	      "product_price": 400,
	    },

	  ];
	}


	function makeStore() {
		const localState = window.localStorage.getItem("shoppingcart");
		const state = localState ? JSON.parse(localState) : initialState;
		const store = new Store({ state, actions });
		store.on("update", null, () => {
			localStorage.setItem("shoppingcart", JSON.stringify(store.state));
		});
		return store;
	}
	function setup() {
		owl.config.mode = "dev";
		App.env.store = makeStore();
		const app = new App();
		 app.mount(document.body);
	}

	whenReady(setup);
