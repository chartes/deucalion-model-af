FROM ponteineptique/pie-flask:v0.0.3

# Add local files
COPY ./ ./
RUN chmod +x boot.sh

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]
