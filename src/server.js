const express = require('express');
const morgan = require('morgan');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8000;

app.use(morgan('dev'));
app.use(express.json());

app.get('/api/health', (_req, res) => {
	res.json({ status: 'ok' });
});

app.use(express.static(path.join(__dirname, '..', 'public')));
app.use((req, res, next) => {
	if (req.path.startsWith('/api')) return next();
	res.sendFile(path.join(__dirname, '..', 'public', 'index.html'));
});

app.listen(PORT, () => {
	console.log(`Server running on http://localhost:${PORT}`);
});
