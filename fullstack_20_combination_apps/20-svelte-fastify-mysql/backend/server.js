import Fastify from "fastify";
import mysql from "mysql2/promise"; async function checkDb(){const c=await mysql.createConnection({host:process.env.MYSQL_HOST,port:Number(process.env.MYSQL_PORT),database:process.env.MYSQL_DATABASE,user:process.env.MYSQL_USER,password:process.env.MYSQL_PASSWORD,connectTimeout:5000});await c.query("SELECT 1");await c.end();}
const app=Fastify({logger:true});
app.get("/health", async (_req,reply)=>{try{await checkDb();return {status:"ok",database:"mysql"}}catch{return reply.code(503).send({status:"error"})}});
app.get("/service/message", async()=>({message:"20-svelte-fastify-mysql is working"}));
await app.listen({host:process.env.HOST||"0.0.0.0",port:Number(process.env.PORT||3000)});
