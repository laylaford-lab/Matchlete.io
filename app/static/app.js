const API = "/api/todos";

const listEl = document.getElementById("todo-list");
const formEl = document.getElementById("todo-form");
const titleEl = document.getElementById("title");
const descEl = document.getElementById("description");

async function fetchTodos() {
	const res = await fetch(API);
	const data = await res.json();
	listEl.innerHTML = "";
	for (const t of data) {
		listEl.appendChild(renderItem(t));
	}
}

function renderItem(todo) {
	const li = document.createElement("li");
	const checkbox = document.createElement("input");
	checkbox.type = "checkbox";
	checkbox.checked = !!todo.is_done;
	checkbox.addEventListener("change", async () => {
		await updateTodo(todo.id, { is_done: checkbox.checked });
	});

	const textWrap = document.createElement("div");
	const title = document.createElement("div");
	title.className = "title" + (todo.is_done ? " done" : "");
	title.textContent = todo.title;
	const desc = document.createElement("div");
	desc.className = "desc";
	desc.textContent = todo.description || "";
	textWrap.appendChild(title);
	textWrap.appendChild(desc);

	const right = document.createElement("div");
	right.className = "right";
	const del = document.createElement("button");
	del.textContent = "Delete";
	del.addEventListener("click", async () => {
		await deleteTodo(todo.id);
	});
	right.appendChild(del);

	li.appendChild(checkbox);
	li.appendChild(textWrap);
	li.appendChild(right);
	return li;
}

async function createTodo(payload) {
	await fetch(API, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(payload),
	});
	fetchTodos();
}

async function updateTodo(id, payload) {
	await fetch(`${API}/${id}`, {
		method: "PATCH",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(payload),
	});
	fetchTodos();
}

async function deleteTodo(id) {
	await fetch(`${API}/${id}`, { method: "DELETE" });
	fetchTodos();
}

formEl.addEventListener("submit", async (e) => {
	e.preventDefault();
	const title = titleEl.value.trim();
	const description = descEl.value.trim();
	if (!title) return;
	await createTodo({ title, description, is_done: false });
	titleEl.value = "";
	descEl.value = "";
});

fetchTodos();

