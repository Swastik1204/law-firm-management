FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY . .
RUN ./mvnw clean package -DskipTests || C:/Tools/apache-maven-3.9.9/bin/mvn.cmd clean package -DskipTests
EXPOSE 8080
CMD ["java", "-jar", "target/lawfirm-app-0.0.1-SNAPSHOT.jar"]
