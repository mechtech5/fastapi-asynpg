import { useNavigate } from "react-router-dom";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";

// Custom Imports
import { login } from "@/api/auth";
import { useStore } from "@/store";

const Login = () => {
  const navigate = useNavigate();
  const setUser = useStore((state: any) => state.setUser);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Mutations
  const mutation = useMutation({
    mutationFn: login,
    onSuccess: (res: any) => {
      console.log(res.data);
      setUser(res.data);
    },
  });

  const handleSubmit = (e: any) => {
    e.preventDefault();
    let formData: any = new FormData();
    formData.append("username", email);
    formData.append("password", password);
    mutation.mutate(formData);
  };

  return (
    <div className="container mx-auto p-4 bg-slate-50">
      <div
        style={{ height: "80vh" }}
        className="flex justify-center items-center"
      >
        <div className="shadow-xl p-10 bg-white">
          <form>
            <div className="mb-4">
              <label className="input input-bordered flex items-center gap-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 16 16"
                  fill="currentColor"
                  className="w-4 h-4 opacity-70"
                >
                  <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
                </svg>
                <input
                  type="text"
                  className="grow"
                  placeholder="Username"
                  onChange={(e) => setEmail(e.target.value)}
                  value={email}
                />
              </label>
            </div>
            <div className="mb-4">
              <label className="input input-bordered flex items-center gap-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 16 16"
                  fill="currentColor"
                  className="w-4 h-4 opacity-70"
                >
                  <path
                    fillRule="evenodd"
                    d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z"
                    clipRule="evenodd"
                  />
                </svg>
                <input
                  type="password"
                  className="grow"
                  placeholder="Password"
                  onChange={(e) => setPassword(e.target.value)}
                  value={password}
                />
              </label>
            </div>
            <a href="" onClick={() => navigate("/forgot-password")}>
              Forgot Password?
            </a>
            <div className="text-center mt-4">
              <button
                onClick={handleSubmit}
                className="btn btn-success text-white"
              >
                Login
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
