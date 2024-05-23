import axios from "axios";

type LoginInput = {
  username: string;
  password: string;
};

type RegisterInput = {
  first_name: string;
  last_name: string;
  email: string;
  password: string;
};

export const login = (payload: LoginInput) => {
  return axios.post("/login", payload);
};

export const register = (payload: RegisterInput) => {
  return axios.post("/register", payload);
};
