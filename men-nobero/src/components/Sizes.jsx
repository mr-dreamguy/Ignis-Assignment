import Size from "./Size";
import { useState, useEffect } from "react";
import api from "../api";

function Sizes({ id }) {
  let [variantData, setVariantData] = useState([]);

  useEffect(() => {
    getVariantData();
  }, []);

  let getVariantData = () => {
    api
      .get(`variant-data/${id}`)
      .then((res) => res.data)
      .then((data) => setVariantData(data))
      .catch((err) => {
        alert(err);
        console.log(err);
      });
  };

  return (
    <>
      <h4>Select Size</h4>
      <div className="flex flex-row mt-2">
        {variantData.map((variant, idx) => (
          <Size key={idx} size={variant.size} quantity={variant.quantity} />
        ))}
      </div>
    </>
  );
}

export default Sizes;
