function Hello(props) {
  return (
    <ul>
      <li>{props.greeting}</li>
      <li><RedButton message="click this, please" /></li>
    </ul>
  );
}

ReactDOM.render(<Hello greeting="Hello world!" />, document.querySelector('#app'));
