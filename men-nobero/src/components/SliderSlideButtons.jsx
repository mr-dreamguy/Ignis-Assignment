function SliderSlideButtons() {
  let style = {
    backgroundColor: "black",
    borderRadius: "5px",
  };
  return (
    <>
      <button
        className="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev"
      >
        <span
          className="carousel-control-prev-icon"
          aria-hidden="true"
          style={style}
        ></span>
        <span className="visually-hidden">Previous</span>
      </button>
      <button
        className="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next"
      >
        <span
          className="carousel-control-next-icon"
          aria-hidden="true"
          style={style}
        ></span>
        <span className="visually-hidden">Next</span>
      </button>
    </>
  );
}

export default SliderSlideButtons;
