import Fastify from "fastify";
import pg from "pg"; const {Client}=pg; async function checkDb(){const c=new Client({host:process.env.PGHOST,port:Number(process.env.PGPORT),database:process.env.PGDATABASE,user:process.env.PGUSER,password:process.env.PGPASSWORD,connectionTimeoutMillis:5000});await c.connect();await c.query("SELECT 1");await c.end();}
const app=Fastify({logger:true});
app.get("/health", async (_req,reply)=>{try{await checkDb();return {status:"ok",database:"postgresql"}}catch{return reply.code(503).send({status:"error"})}});
app.get("/service/message", async()=>({message:"13-vue-fastify-postgres is working"}));
await app.listen({host:process.env.HOST||"0.0.0.0",port:Number(process.env.PORT||3000)});
