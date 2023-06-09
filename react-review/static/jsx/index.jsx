function Card(props) {
	const color = (props.suit === 'heart' || props.suit === 'diamond') ?
		'danger' : 'black';

	const suits = {
		heart: 'Hearts',
		diamond: 'Diamonds',
		spade: 'Spades',
		club: 'Clubs'
	};

	return (
		<div className="col-3 mb-3">
			<div className={`card text-${color}`}>
				<div className="card-header text-start">
					<u>{props.abrev}</u>&nbsp;
					<i class={`bi bi-suit-${props.suit}-fill`}></i>
				</div>
				<div className="card-body text-center">
					<h3>{props.name} of {suits[props.suit]}</h3>
				</div>
				<div className="card-footer text-end">
					<i class={`bi bi-suit-${props.suit}-fill`}></i>
					&nbsp;<u>{props.abrev}</u>
				</div>
			</div>
		</div>
	);
}


function shuffleArray(arr, x) {
	// shuffle array x times
	const randomize = () => Math.random() - 0.5;
	for (let i = 1; i <= x; i++) {
		arr.sort(randomize)
	}
	return arr;
}

function CardDeck() {
	const [cards, setCards] = React.useState([]);

	React.useEffect(() => {
		fetch('/api/cards.json')
			.then((response) => response.json())
			.then((cardsArr) => {
				setCards(cardsArr);
			})
	}, []);

	function shuffle() {
		const shuffledCards = shuffleArray(cards, 5);
		setCards([...shuffledCards]);
	}

	const cardComponents = cards.length === 0 ?
		(<p><span className="spinner-border"/> Loading...</p>) :
		(cards.map((card) => {
			return (
				<Card
					suit={card.suit}
					name={card.name}
					abrev={card.abrev}
					value={card.value}
					key={card.abrev + '-' + card.suit}
				/>
			);
		}));

	return (
		<div className="row">
			<div className="col border rounded py-2">
				<button
					className="btn btn-warning"
					type="button"
					onClick={shuffle}
				>
					Shuffle the deck
				</button>
				<h2>Card components:</h2>
				<div className="row mt-4">{cardComponents}</div>
			</div>
		</div>
	);
}


function getRandomNum(max) {
	// get a random number between 1 and max, inclusive
	return Math.ceil(Math.random() * max);
}

function Die(props) {
	const [dieValue, setDieValue] = React.useState('?');

	function roll() {
		const rollResult = getRandomNum(props.sides);
		setDieValue(rollResult);
	}

	return (
		<button
			className="btn btn-success me-2 px-4"
			type="button"
			onClick={roll}
		>
			<p>d{props.sides}</p>
			<h2>{dieValue}</h2>
		</button>
	);
}


function ClickCounter(props) {
	const [currentCount, setCurrentCount] = React.useState(props.initialCount);

	function incrementCount() {
		setCurrentCount((current) => current + 1);
	}

	return (
		<div className="row mb-5">
			<div className="col border rounded py-2">
				<h2>{currentCount}</h2>
				<button
					className="btn btn-primary"
					type="button"
					onClick={incrementCount}
				>
					<i className="bi bi-hand-index-thumb"></i>
					&nbsp;Click me to increase the count
				</button>
			</div>
		</div>
	);
}


function App() {
	const diceSides = [4, 6, 8, 10, 12, 20];
	const dieComponents = diceSides.map((num) => {
		return <Die sides={num} key={num} />
	});

	return (
		<>
			<h1>ClickCounter component:</h1>
			<ClickCounter initialCount={0} />

			<h1>Die components:</h1>
			<div className="row mb-5">
				<div className="col border rounded py-2">
					{dieComponents}
				</div>
			</div>

			<h1>CardDeck component:</h1>
			<CardDeck />
		</>
	);
}


ReactDOM.render(<App />, document.getElementById('root'));
