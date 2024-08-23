function SliderButton({ index }) {
  return (
    <button
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide-to={"" + index}
      className="active"
      aria-current="true"
      aria-label={"Slide " + (index + 1)}
    ></button>
  );
}

export default SliderButton;
