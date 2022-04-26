function RedButton(properties) {
  const styles = {
    backgroundColor: "red",
    color: "white"
  };

  return (
    <div>
      <button type="button" style={styles}>
      {properties.msg}
      </button>
    </div>
  );
}

// ReactDOM.render(<Button message="Click me, please!" bgColor="green" color="black" />, document.querySelector('#root'));
ReactDOM.render(
  (
    <div>
      <RedButton msg="Click me" />
      <RedButton msg="Or click me" />
    </div>
  ),
  document.querySelector('#root')
);
