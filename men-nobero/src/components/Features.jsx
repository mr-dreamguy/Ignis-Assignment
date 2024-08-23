function Features({ product }) {
  let features = [
    { key: "fit", value: "Fit" },
    { key: "fabric", value: "Fabric" },
    { key: "pattern", value: "Pattern" },
    { key: "neck", value: "Neck" },
    { key: "sleeve", value: "Sleeve" },
    { key: "length", value: "Length" },
    { key: "waistrise", value: "Waist-Rise" },
    { key: "waistband", value: "Waistband" },
    { key: "bottomwearlength", value: "Bottom Wear Length" },
  ];

  return (
    <div className="mt-3 mb-3">
      <h4>Features</h4>
      {features.map((item) => (
        <div>
          {product[item.key] == null ? null : (
            <div>
              {item.value} :- &nbsp; {product[item.key]}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

export default Features;
