import Sizes from "./Sizes";
import "../styles/Variants.css";
import { useState, useEffect } from "react";
import api from "../api";

function Variants({ id }) {
  let [index, setIndex] = useState(0);
  let [variants, setVariants] = useState([]);

  useEffect(() => {
    getVariants();
  }, [id]);

  let getVariants = () => {
    api
      .get(`/variants/${id}`)
      .then((res) => res.data)
      .then((data) => setVariants(data))
      .catch((err) => {
        alert(err);
        console.log(err);
      });
  };

  return (
    <>
      {variants.length > 0 ? (
        <div>
          <h4>
            Select Color - <span>{variants[index].color}</span>
          </h4>
          <div className="flex flex-row mb-3">
            {variants.map((variant, idx) => {
              return (
                <div key={idx} className="d-inline">
                  <input
                    type="radio"
                    className="btn-check"
                    name="variants"
                    autoComplete="off"
                    id={"variant" + idx}
                    checked={idx === index}
                    value={variant.color}
                    onChange={() => setIndex(idx)}
                  />
                  <label className="btn" htmlFor={"variant" + idx}>
                    <img
                      className="img-fluid"
                      src={variant.image}
                      style={index === idx ? { opacity: 1 } : null}
                    />
                  </label>
                </div>
              );
            })}
          </div>
          <Sizes id={variants[index].id} />
        </div>
      ) : null}
    </>
  );
}

export default Variants;
