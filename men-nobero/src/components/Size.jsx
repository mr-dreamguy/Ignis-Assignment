function Size({ size, quantity }) {
  let attrib = {
    type: "radio",
    className: "btn-check",
    name: "sizes",
    id: size,
    autoComplete: "off",
  };

  let styles = {
    width: "100px",
    textDecoration: quantity === 0 ? "line-through" : null,
  };
  return (
    <>
      {quantity === 0 ? <input {...attrib} disabled /> : <input {...attrib} />}
      <label
        className="btn btn-outline-secondary"
        htmlFor={size}
        style={styles}
      >
        {size}
      </label>
    </>
  );
}

export default Size;
