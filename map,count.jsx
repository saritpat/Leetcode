import React, { useState } from "react";

export const App = () => {
    const [data, setData] = useState(["A", "B", "C"]);

    return (
        <div>
            {data.map((item, index) => {
                <div key={index}>Item : {item}</div>;
            })}
        </div>
    );
};

import React, { useState } from "react";

export const Count = () => {
    const [count, setCount] = useState(0);

    return (
        <div>
            Count : {count}
            <button onClick={() => setCount(count + 1)}>+</button>
            <button onClick={() => setCount(count - 1)}>-</button>
        </div>
    );
};
