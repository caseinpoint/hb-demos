function ClickCounter(props) {
  const [currentCount, setCurrentCount] = React.useState(props.initialCount);
  console.log(currentCount);

  const handleClick = () => {
    setCurrentCount(currentCount + 1);
  };

  return (
    <div>
      <div>{currentCount}</div>
      <button type="button" onClick={handleClick}>
        Click me to increase the count
      </button>
    </div>
  );
}

ReactDOM.render(<ClickCounter initialCount={0} more="things" />, document.querySelector('#root'));

















/* bonus demo: */
function Clock(props) {
  const [date, setDate] = React.useState(new Date());

  const id = setInterval(() => { setDate(new Date()); }, 1000);

  return (
    <div>
      <h2>Hello! It is currently:</h2>
      <h3>{date.toLocaleString()}</h3>
    </div>
  );
}

// ReactDOM.render(<Clock />, document.querySelector('#root'));
